import React, {useState} from 'react';
import {FormControl, InputLabel, MenuItem, Select, SelectChangeEvent} from "@mui/material";
import {useGetFormsQuery} from "./formApiSlice.ts";
import {Permission} from "../permissions/Permission.tsx";

interface FormType {
    uid: string,
    name: string
}

function Form() {
    const [selectedForm, setSelectedForm] = useState('')

    const {data: formsData} = useGetFormsQuery(null)
    const formList: FormType[] = formsData?.results
    const handleChange = (evt: SelectChangeEvent) => {
        setSelectedForm(evt.target.value);
    }
    return (
        <div>
            <FormControl fullWidth>
                <InputLabel id="form-list-label">Form List</InputLabel>
                <Select
                    labelId="form-list-label"
                    label="Form List"
                    value={selectedForm}
                    onChange={handleChange}
                >
                    {formList?.map((form) => (
                        <MenuItem key={form.uid} value={form.uid}>{form.name}</MenuItem>
                    ))}
                </Select>
            </FormControl>
            <Permission formId={selectedForm}/>
        </div>
    );
}

export default Form;