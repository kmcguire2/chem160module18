args <- commandArgs(trailingOnly = T) #only the args after the script name
#test that there is only one argument
if (length(args)!=1){
	stop("Requires 1 argument, initial N")
}
N <- as.integer(args[1]) #convert to an integer
steps <- 0
while (N !=1) {
	cat (N, "\n")
	if (N%%2==0) {
		N <- N/2
	} else {
		N <- 3*N+1
	}
	steps <- steps + 1
}
cat("steps=", steps, "\n")
