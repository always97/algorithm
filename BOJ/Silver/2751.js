const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input.map((e) => Number(e));

// function quickSort(arr,l,r) {
//   let left = l;
//   let right = r;
//   let pivot = arr[Math.floor((l+r)/2)];
//   while(left<=right) {
//     while(arr[left] < pivot) left++;
//     while(arr[right] > pivot) right--;
//     if(left<=right) {
//       let tmp = arr[left];
//       arr[left] = arr[right];
//       arr[right] = tmp;
//       left++;
//       right--;
//     }
//   }
//   if(l<right) quickSort(arr,l,right);
//   if(r>left) quickSort(arr,left,r);

// }

// quickSort(arr,0,arr.length-1);

function mSort(arr,L,R) {
if(L==R) return;

  let mid = Math.floor((L+R)/2);
  mSort(arr,L,mid);
  mSort(arr,mid+1,R);
  let left = L;
  let right = mid+1;
  let tmp = [];
  while(left<= mid &&right <=R) {
    if(arr[left]<=arr[right]) {
      tmp.push(arr[left]);
      left++;
    }else {
      tmp.push(arr[right]);
      right++;
    }
  }
  while(left<=mid) {
    tmp.push(arr[left]);
    left++;
  }
  while(right<=R) {
    tmp.push(arr[right]);
    right++;
  }
  for(let i = 0; i<tmp.length; i++) {
    arr[L+i] = tmp[i];
  }
}
mSort(arr,0,arr.length-1);
let answer = '';
arr.map((v)=> answer+= v+"\n");

console.log(answer);