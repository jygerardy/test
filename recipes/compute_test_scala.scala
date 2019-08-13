import com.dataiku.dss.spark._
import org.apache.spark.SparkContext
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.functions._

val sparkConf    = DataikuSparkContext.buildSparkConf()
val sparkContext = new SparkContext(sparkConf)
val sqlContext   = new SQLContext(sparkContext)
val dkuContext   = DataikuSparkContext.getContext(sparkContext)

// Recipe inputs
val companylist_prepared_by_Sector = dkuContext.getDataFrame(sqlContext, "companylist_prepared_by_Sector")

// TODO: Write here your actual code that computes the outputs
val test_scala = replace_me_by_your_code

// Recipe outputs
dkuContext.save("test_scala", test_scala);
