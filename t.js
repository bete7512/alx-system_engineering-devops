var MyQueue = function() {
    this.stack = []
    this.poped = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.stack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    if(!this.poped.length){
        while(this.stack.length){
            this.poped.push(this.stack.pop())
        }
    }
    return this.poped.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if(!this.poped.length){
        while(this.stack.length){
            this.poped.push(this.stack.pop())
        }
    }
    return this.poped[this.stack.length-1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return !this.stack.length && !this.poped.length
};
