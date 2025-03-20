import json

class LightMap:
    def __init__(self, ownerComp) -> None:
        self.ownerComp=ownerComp
        print(self.__class__.__name__)
        pass


    def UpdateMapping(self):
        fixture_ops = self.ownerComp.findChildren(tags=['map'])
        
        for op in fixture_ops:
            op.destroy()
        

        json_data=str(self.ownerComp.dock.op("LightPatchJson").text)

        data = json.loads(json_data)
        for i, element in enumerate (data['dmxpatch']):
            name=element['name']
            if 'control' in element:
                for i1, item in enumerate(element['control']):
                    u=item['x']
                    v=item['y']
                    src_comp=self.ownerComp.op("protoPixel")
                    new_comp = self.ownerComp.copy(src_comp, name=name)
                    new_comp.tags.add('map')
                    new_comp.nodeX=200*i
                    new_comp.par.Fixture=name
                    new_comp.par.Map=item['source']
                    new_comp.par.Uvu=u-1
                    new_comp.par.Uvv=v-1
                    new_comp.par.Parsmap=json.dumps(item['map'])
                    new_comp.op("route").clear()
                    new_comp.op("route").appendRow(["name", "index", "path", "parameter", "enable"])
                    for i2, (src, dst) in enumerate(item['map'][0].items()):
                        new_comp.op("route").appendRow([src,i2,self.ownerComp.dock.op(name).path, dst, "1"])
                    new_comp.op("PIXEL").export=True

            # if "x" in element and "y" in element:
                

            #     # print (element['name'])
                pass
            pass

    def UpdateChan(self, fixtureName, parsMap,chname, val):
        fixtureOp=self.ownerComp.dock.op(fixtureName)
        if fixtureOp is not None:
            pars=json.loads(str(parsMap))
            
            for src, dst in pars[0].items():
                # print (hasattr(fixtureOp.par, dst))
                pass
                # print ("{}, {}".format(key, value))
            fixtureOp.par.White=val
        pass