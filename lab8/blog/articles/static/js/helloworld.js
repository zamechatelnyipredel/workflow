const groupmates = [
    {
        "name": "Альберт",
        "group": "БСТ2258",
        "age": 23,
        "marks": [4, 3, 4, 5, 5]
    },
    {
        "name": "Полина",
        "group": "БСТ2253",
        "age": 23,
        "marks": [4, 3, 3, 4, 5]
    },
    {
        "name": "Полина",
        "group": "БСТ2253",
        "age": 31,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Сергей",
        "group": "БСТ2253",
        "age": 28,
        "marks": [4, 3, 5, 4, 5]
    }
];

const rpad = function (str, length) {
// js не поддерживает добавление нужного количества символов
// справа от строки, то есть аналога ljust из языка Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};
const printStudents = function (students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
// был выведен заголовок таблицы
    for (let i = 0; i <= students.length - 1; i++) {
// в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates);

function filter(students, group) {
    const list = [];
    for (let i = 0; i < students.length; i++) {
        if (students[i].group === group) {
            list.push(students[i]);
        }
    }
    return list;
}

const filterStudents = filter(groupmates, "БСТ2253");
console.log("Студенты группы БСТ2253:");
console.log(filterStudents);