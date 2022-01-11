function solution(board, moves) {
  let answer = 0;
  let basket = [];

  for (let i = 0; i < moves.length; i++) {
    let j = 0;
    while (j < board.length) {
      if (board[j][moves[i] - 1] != 0) {
        if (basket.length != 0) {
          if (basket[basket.length - 1] === board[j][moves[i] - 1]) {
            board[j][moves[i] - 1] = 0;
            basket.pop();
            answer += 2;
            break;
          }
        }
        basket.push(board[j][moves[i] - 1]);
        board[j][moves[i] - 1] = 0;
        break;
      } else {
        j++;
      }
    }
  }

  return answer;
}