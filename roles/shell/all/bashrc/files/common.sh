# tools aliases
function ag() {
    grep -rnw '.' -e "$1"
}

# ls aliases
alias ll='ls -lF'
alias lla='ls -alF'
alias la='ls -A'
alias l='ls -CF'
