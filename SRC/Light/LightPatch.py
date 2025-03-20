import json

class LightPatch:
    def __init__(self, ownerComp) -> None:
        self.ownerComp=ownerComp
        print(self.__class__.__name__)
        pass


    def UpdatePatch(self):

        fixture_ops = self.ownerComp.findChildren(tags=['fixture'])
        
        for op in fixture_ops:
            op.destroy()
        
        json_data=str(self.ownerComp.op("LightPatchJson").text)

        data = json.loads(json_data)

        for i, element in enumerate (data['dmxpatch']):
            fixture=element['fixture']
            name=element['name']
            outputnode=element['outputnode']
            src_comp = self.ownerComp.op('FixturesLibrary').op(fixture)
            new_comp = self.ownerComp.copy(src_comp, name=name)
            new_comp.tags.add('fixture')
            if fixture=="space":
                new_comp.par.Amount=element['amount']
            target_comp = self.ownerComp.op(outputnode)
            
            new_comp.outputConnectors[0].connect(target_comp)

            new_comp.nodeX=200*i

            