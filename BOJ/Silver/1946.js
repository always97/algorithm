const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let tc = input[0];
let idx = 1;

while (tc--) {
  const num = input[idx++];
  const applicant = [];
  for (let i = 0; i < num; i++) {
    let data = input[idx++].trim().split(' ');
    applicant.push({ "first": Number(data[0]), "second": Number(data[1]) });
  }
  applicant.sort((a, b) => (a.first - b.first));
  let pass = 1;
  let cut = applicant[0].second;
  for (let i = 1; i < num; i++) {
    if (cut > applicant[i].second) {
      pass++;
      cut = applicant[i].second;
    }
  }
  console.log(pass);
}
