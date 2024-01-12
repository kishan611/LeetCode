/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function(moves) {
    let arr=[["","",""],["","",""],["","",""]];
    let count=0;
    let winPattern=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,4,8],
        [2,4,6],
        [0,3,6],
        [1,4,7],
        [2,5,8]
    ];
    for(let i of moves){
        if(count%2==0){
            arr[i[0]][i[1]]="X";
        }
        else{
            arr[i[0]][i[1]]="O";
        }
        count++;
    }
    let res=[...arr[0],...arr[1],...arr[2]];
    for(pat of winPattern){
        let pos1=res[pat[0]];
        let pos2=res[pat[1]];
        let pos3=res[pat[2]];
        if(pos1==pos2 && pos2==pos3){
            if(pos1=="X"){
                return "A";
            }
            else if(pos1=="O"){
                return "B";
            }
        }
    }
    if(count<9){
        return "Pending";
    }
    else{
        return "Draw";
    }
};