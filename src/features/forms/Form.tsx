import React, {useEffect, useState} from 'react';
import {FormControl, InputLabel, MenuItem, Select, SelectChangeEvent} from "@mui/material";
import {useGetFormsQuery} from "./formApiSlice.ts";
import {Permissions} from "../permissions/Permissions.tsx";
import {setForms} from "./formSlice.ts";
import {useDispatch} from "react-redux";
import {FormType} from "./form.model.ts";


function Form() {
    const [selectedFormId, setSelectedFormId] = useState('')
    const dispatch = useDispatch()


    // const formList: FormType[] = [] as FormType[]


    const {data: formsData} = useGetFormsQuery(null)
    const formList: FormType[] = formsData?.results
    // const formList: FormType[] = useMemo(() => formsData?.results, [formsData?.results])

    useEffect(() => {
        dispatch(setForms(formList))
    }, [formList])

    const handleChange = (evt: SelectChangeEvent) => {
        setSelectedFormId(evt.target.value);
    }

    return (
        <div className='m-2 md:mx-8 lg:m-12 mt-2'>
            <div className='my-3 text-xl'>Select Form</div>
            <FormControl fullWidth>
                <InputLabel id="form-list-label">Form List</InputLabel>
                <Select
                    labelId="form-list-label"
                    label="Form List"
                    value={selectedFormId}
                    onChange={handleChange}
                >
                    {formList?.map((form) => (
                        <MenuItem key={form.uid}
                                  value={form.uid}>{form.name}</MenuItem>
                    ))}
                </Select>
            </FormControl>
            <Permissions formId={selectedFormId}/>
        </div>
    );
}

export default Form;