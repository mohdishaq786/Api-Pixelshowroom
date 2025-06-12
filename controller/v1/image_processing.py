from fastapi import APIRouter
from services.remove_bg import remove_bg
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from services.masking_plate import masking_license_plate
from utils.util import base64_to_pil, pil_to_base64
from services.super_imposer import superimpose_with_resize
from services.logo import paste_logo
router = APIRouter()

class Input(BaseModel):
    image_str:str
    background_str:str = Field(None)
    logo_str:str=Field(None)
    logo_position:str=Field(None)


@router.post('/imageProcessing')
def imageProcessing(Input:input):
    input_img_str = input.image_str
    input_img = base64_to_pil(input_img_str)

    output_img = masking_license_plate(input_img)
    output_img = remove_bg(output_img)

    if input.background_str:
        background_img_pil=base64_to_pil(input.background_str)
        output_img=superimpose_with_resize(background_img_pil, output_img)
    
    if input.logo_str:
        logo_img=base64_to_pil(input.logo_str)
        output_img=paste_logo(output_img,logo_img,input.logo_position)
        

    output_img_str = pil_to_base64(output_img)

    return JSONResponse(content={"output":output_img_str},status_code=201, media_type="application/json")
