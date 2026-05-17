console.log("%c home js", "color: blue;")


const form_obj = document.getElementById("create-form");

console.log(form_obj);
function generateTem(new_plan){
  return ` <li
           class="plan list-group-item bg-light d-flex align-items-center justify-content-between custom-list"
          >
            <span class="item-text">${new_plan.content}</span>
            <div>
              <button
                data-id="${new_plan.id}"
                class="edit-me btn btn-success btn-sm mr-1 custom-radius"
              >
                <i style="margin-right: 5px" class="bi bi-pencil-square"></i
                >Edit
              </button>
              <button
                data-id="${new_plan.id}"
                class="delete-me btn btn-danger btn-sm custom-radius"
              >
                <i style="margin-right: 5px" class="bi bi-trash"></i> Delete
              </button>
            </div>
          </li>`

}
form_obj.addEventListener("submit", function (e) {
   // stop traditional API
    e.preventDefault();
    console.log("Trad API stop");
    const input_value = document.getElementById("create-field").value;

    
    console.log('step1: frontending js dan backendga *> REST API req *> jonatilindi')
  // start REST api
    axios
    .post("/create-plan", {content: input_value })
    .then((res)=>{
        console.log('ste6: fronted backendan > API res ni > qabul qildi')
        console.log('axios response: ' , res)
        const { status , result } = res.data

        const new_plan = {
            id:  result,
            content: input_value
        };
        console.log('step7: mutade js page')
        
        document.getElementById('item-list').insertAdjacentHTML('beforeend', generateTem(new_plan) )
        document.getElementById("create-field").value = '';
        document.getElementById("create-field").focus();

        console.log(result, input_value)

    })
    .catch((err)=>{
        console.log('creating plan is fail' , err)
    })
});

document.addEventListener('click', function(e){
  console.log("event", e)
  if (e.target.classList.contains('edit-me')){
    const user_input = prompt('change :', 
      e.target.parentElement.parentElement.querySelector(".item-text").innerHTML)

      if (user_input){
        axios.post("/update-plan", {
          id: e.target.getAttribute("data-id"),
          new_plan: user_input
        })
        .then((res)=>{
          console.log('Axios res update:', res);
          const {status , result} = res.data;

          e.target.parentElement.parentElement.querySelector(".item-text").innerHTML = user_input
          console.log(result , user_input)
        })
        .catch((err)=>{
          console.log('UPdating plan error:', err)

        })
      }
    }
})