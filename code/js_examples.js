// Microsoftalion: 10^10000 с использованием BigInt
const MICROSOFTALION = BigInt("1" + "0".repeat(10000));

// Основные операции
function getFirstDigits(bigInt, n = 50) {
    const str = bigInt.toString();
    return str.substring(0, n);
}

function getLastDigits(bigInt, n = 50) {
    const str = bigInt.toString();
    return str.substring(str.length - n);
}

function countDigits(bigInt) {
    return bigInt.toString().length;
}

// Демонстрация
console.log(`Первые 50 цифр: ${getFirstDigits(MICROSOFTALION)}...`);
console.log(`Последние 50 цифр: ${getLastDigits(MICROSOFTALION)}`);
console.log(`Всего цифр: ${countDigits(MICROSOFTALION)}`);
