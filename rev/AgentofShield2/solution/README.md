# Agent of Shield 2
## Writeup

- after decompiling with ghidra and looking at the code we will find a function named `generate_flag()` inside it there is a function `hmmm()` that calls exit(1) we can patch and replace the call with `NOP`
the agent nam is `Daisy_Johnson` it is declared as a global variable you can find it in th exports list under the name of `agent`


## Flag
> Alphabit{you-270-455-agent}

