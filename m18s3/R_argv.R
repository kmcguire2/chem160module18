args <- commandArgs(trailingOnly=T) #only the arguments that come after the script name
cat("Number or arguments:", length(args), "\n")
for (i in args) {
	cat(i, "\n")
}
