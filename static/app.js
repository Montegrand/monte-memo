async function editMemo(e){
    const id = e.target.dataset.id;
    const editInput = prompt('수정할 값을 입력해주세요.');

    const res = await fetch(`/memos/${id}`,{
        method: 'PUT',
        headers: {
            "Content-Type": "application/json",
        }, body: JSON.stringify({
            id: id,
            content: editInput,
        }),
    });
    readMemo();
}

function displayMemo(memos){
    const ul = document.querySelector('#memo-ul');
    const li = document.createElement('li');
    const editBtn = document.createElement('button');

    li.innerText = `[id: ${memos.id}] ${memos.content}`;
    editBtn.innerText = '수정하기';
    editBtn.dataset.id = memos.id
    editBtn.addEventListener('click',editMemo);
    li.appendChild(editBtn);
    ul.appendChild(li);
}

async function readMemo(){
    const res = await fetch('/memos');
    const jsonRes = await res.json();
    const ul = document.querySelector('#memo-ul');
    ul.innerHTML = '';
    jsonRes.forEach(displayMemo);
}

async function createMemo(value){
    const res = await fetch('/memos',{
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: new Date().getTime(),
            content: value,
        }),
    });

    const jsonRes = await res.json();
    readMemo();
}

function handleSubmit(e){
    e.preventDefault();

    const input = form.querySelector('#memo-input');
    createMemo(input.value);
    input.value = '';
};

const form = document.querySelector('#memo-form');
form.addEventListener('submit',handleSubmit);

readMemo()