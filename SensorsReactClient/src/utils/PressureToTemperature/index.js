import R404ADataSheet from './tables/R404A.json';
import R134ADataSheet from './tables/R134A.json';

function jsonToArray(dataSheet) {
    var result = [];
    for(var i in dataSheet) {
        result.push([i, dataSheet[i]]);
    }
    return result;
}

export default function getTemperatureFromPressure(refrigerant, pressure) {
    if (refrigerant === "R404A") {
        var pressuresList = jsonToArray(R404ADataSheet);
    } 
    else if (refrigerant === "R134A") {
        var pressuresList = jsonToArray(R134ADataSheet);
    } else {
        return {err: 'this refrigerant is not supported'};
    }

    for(var i in pressuresList) {
        i = parseInt(i);
        if (i === pressuresList.length - 1) {
            return {err: 'Out of range'};
        }
        var range_begin = parseFloat(pressuresList[i][0]);
        var range_end = parseFloat(pressuresList[i + 1][0]);

        if (pressure >= range_begin && pressure <= range_end) {
            // Time for maths 
            var x1 = range_begin;
            var x2 = range_end;

            var y1 = pressuresList[i][1];
            var y2 = pressuresList[i + 1][1];

            var a = (y2 - y1) / (x2 - x1);
            var b = (y1 - a * x1);

            return a * pressure + b
        }
    }
}