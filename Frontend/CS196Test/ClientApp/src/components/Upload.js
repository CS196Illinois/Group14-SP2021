import React, { Component } from 'react';

export class Upload extends Component
{
    static displayName = Upload.name;
    
    constructor(props)
    {
        super(props);
        this.fileInput = React.createRef();
    }

    handleUpload(event)
    {
        event.preventDefault();
        alert(
            `Selected file - ${this.fileInput.current.files[0].name}`
        );
    }

    
    render()
    {
        return (
            <div>
                <div>
                    <h3>Upload Image Here</h3> <br />
                </div>
                <form onSubmit={this.handleUpload}>
                    <input
                        type="file"
                        accept="image/*"
                        ref={this.fileInput}
                    />
                </form>
                {/* ALLOW USER TO PREVIEW IMAGE??? */}
            </div>
        );
    }
}


