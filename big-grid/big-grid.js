
songs_table = document.getElementById('songstable');
console.log('hi');
for(var i=3; i<9; j++) {
    gridRow = document.createElement('tr');
    for(var j=3; j<9; j++) {
        gridCell = document.createElement('td');
        gridCell.setAttribute('id',''+i+','+j);
        gridRow.appendChild(gridCell);
    }
    songs_table.appendChild(gridRow);
}