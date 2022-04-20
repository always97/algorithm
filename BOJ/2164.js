const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(item) {
    const node = new Node(item);
    if (this.size === 0) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size++;
  }

  pop() {
    if (this.length === 0) {
      return false;
    }
    const data = this.head.item;
    this.head = this.head.next;
    this.size--;

    return data;
  }
}

const answer = solution(+input[0]);

function solution(n) {
  const queue = new Queue();
  for (let i = 1; i <= n; i++) {
    queue.push(i);
  }
  while (queue.size > 1) {
    queue.pop();
    const front = queue.pop();
    queue.push(front);
  }
  return queue;
}

console.log(answer.head.item);