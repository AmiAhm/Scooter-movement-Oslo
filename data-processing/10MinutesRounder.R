setwd(getSrcDirectory()[1])
df <- read.csv("../processed-data/output.csv")
startTime <- df$time[1]
df$time <- ((df$time - startTime)  %/%  600) * 600 + startTime
df <- df[ order(df$time , decreasing = FALSE ),]
df <- df %>% group_by(operator, id, time) %>% filter(row_number()==1)
write.csv(df, "../processed-data/output10min.csv")
