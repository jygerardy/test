const graphContainer = document.getElementById('graph-container');

function score() {
  let featuresJson = $('#features-field').val();
  let selectedVariable = $('#selected').val();
  let counterFactualsRaw = $('#counter-factuals').val();
  let increment = $('#increment').val();
  let isCategorical = $('input[name=feature-type]:checked').val() == 'Categorical';

  resetOutputs();

  checkInput(selectedVariable, featuresJson); //check if those two inputs are missing or not well formatted

  let counterFactuals = parseCounterFactuals(counterFactualsRaw, increment, isCategorical);


  graphContainer.innerHTML = '<div class="graph-placeholder">Scoring in progress. Wait...</div>';
  webappBackend.get('score', {
      featuresJson: featuresJson,
      counterFactuals: counterFactuals,
      selectedVariable: selectedVariable

    })
    .catch(err => displayAndThrowError(err, null))
    .then(response => extractPredictions(response))
    .then(predictions => displayGraph(predictions, counterFactuals, isCategorical))
};

function checkInput(selectedVariable, json) {
  if (isBlank(selectedVariable)) {
    let message = "Missing variable of interest. Enter the variables you would like to see vary";
    displayAndThrowError(message, 'selected-feature');
  };
  try {
    JSON.parse(json);
  } catch (e) {
    let message = "JSON missing or not well formatted";
    displayAndThrowError(message, 'features');
    throw e;
  }
}


function resetOutputs() {
  graphContainer.innerHTML = ''; //clear existing graph
  $('.error-block').remove();
}

function displayAndThrowError(errorMsg, field) {
  let elt;
  if (field) {
    elt = $(`.field-${field}`);
  } else {
    elt = $('#text-output');
  }
  const errorElt = $('<div class="error-block"></div>').text(errorMsg);
  $('.graph-placeholder').remove();
  $('.error-block', elt).remove(); // Note that it's not impossible, clicking fast twice on score that 2 errors happen, let's not duplicate (has the side effect of only displaying one error message per call. Sounds ok)
  elt.append(errorElt);
  throw new Error(errorMsg);
}


function extractPredictions(resp) {
  return resp.data.results.map(pred => pred.prediction);
}


function displayGraph(results, counterFactuals, isCategorical) {
  resetOutputs();
  let data = {
    x: counterFactuals,
    y: results
  };

  if (isCategorical) {
    data.type = 'bar'
    data.text = results.map(String)
  } else {
    data.type = 'scatter'
  }
  console.warn('display graph', graphContainer, data)
  Plotly.newPlot(graphContainer, [data], {
    scrollZoom: true,
    showSendToCloud: true
  });
}


function parseCounterFactuals(counterFactualsRaw, increment, isCategorical) {
  if (isCategorical) {
    return parseCounterFactualsCat(counterFactualsRaw);
  } else {
    return parseCounterFactualsNum(counterFactualsRaw, increment);
  }
}


function parseCounterFactualsCat(counterFactualsRaw) {
  if (isBlank(counterFactualsRaw)) {
    let message = "Field is empty!";
    displayAndThrowError(message, 'error-block-counter-factuals');
  };

  let cfComma = counterFactualsRaw.split(",");
  for (let txt of cfComma) {
    if (isBlank(txt)) {
      let message = "Missing value in your comma-separated list";
      displayAndThrowError(message, 'counter-factuals');
    }
  };

  return cfComma;
}


function parseCounterFactualsNum(counterFactualsRaw, increment) {
  if (isBlank(counterFactualsRaw)) {
    let message = "Field is empty";
    displayAndThrowError(message, 'counter-factuals');
  } else {
    let cfComma = counterFactualsRaw.split(",");
    let cfDash = counterFactualsRaw.split("-");

    if (cfComma.length > 1 && cfDash.length > 1) {
      let message = "Mix of comma(s) and range(s). Only one type allowed";
      displayAndThrowError(message, 'counter-factuals');

    } else if (cfComma.length > 1) {
      // this is a comma separated list
      for (let txt of cfComma) {
        if (isBlank(txt)) {
          //  handle empty values before "Numberizing" them as
          //  empty values are converted to 0 when Numberizing them
          let message = "Missing number in your comma-separated list";
          displayAndThrowError(message, 'counter-factuals');
        }
      };
      cfComma = cfComma.map(x => Number(x));
      for (let num of cfComma) {
        if (isNaN(num)) {
          let message = "One of the inputs in your comma-separated list is not a number";
          displayAndThrowError(message, 'counter-factuals');
        }
      };
      return cfComma;

    } else if (cfDash.length == 2) {

      for (let txt of cfDash) {
        if (isBlank(txt)) {
          //  handle empty values before "Numberizing" them as
          //  empty values are converted to 0 when Numberizing them
          let message = "Missing upper or lower bound in your range";
          displayAndThrowError(message, 'counter-factuals');
        }
      };
      // this is a range. THere should only be one
      cfDash = cfDash.map(x => Number(x));
      for (let num of cfDash) {
        if (isNaN(num)) {
          let message = "One of the inputs in your range is not a number"
          displayAndThrowError(message, 'counter-factuals');
        }
      }
      return convertRangeToList(cfDash, increment);

    } else {
      let message = "Something wrong. Possibly not enough numbers or more than one range";
      displayAndThrowError(message, 'counter-factuals');
    }
  };
}


function convertRangeToList(range, increment) {
  let minimum = Math.min(...range);
  let maximum = Math.max(...range);

  if (isBlank(increment) || isNaN(increment)) {
    let message = "When using a range, be sure to include a numerical increment";
    displayAndThrowError(message, 'increment');
  };

  let values = [];
  for (let v = minimum; v <= maximum; v += increment) {
    values.push(v);
  }
  return values
}


function init() {
  try {
    dataiku.checkWebAppParameters();
  } catch (e) {
    webappMessages.displayFatalError(e.message + ' Go to settings tab.');
    throw e;
  }
  $('#scoring-button').click(score);
  $('input[name=feature-type]').change(function() {
    let isCategorical = $('input[name=feature-type]:checked').val() == 'Categorical';
    if (isCategorical) {
      $('.field-increment').hide();
    } else {
      $('.field-increment').show();
    }
  });
}



init();
