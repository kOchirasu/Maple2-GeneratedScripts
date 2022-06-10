using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003559: 
/// </summary>
public class _11003559 : NpcScript {
    internal _11003559(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0920165106000914$ 
                // - ((China Only)) Nihao! Welcome, $MyPCName$!
                return true;
            case 10:
                // $script:0920165106000915$ 
                // - Nihao, $MyPCName$! I am $npcName:11003559[gender:1]$ from China!
                switch (selection) {
                    // $script:0920165106000916$
                    // - ((China Only)) How'd you end up coming here?
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:0920165106000917$ 
                // - ((China Only)) Global MapleStory 2!
                //   I came to meet the Korean adventurers in celebration of MapleStory 2's launch in China!
                //   I'm glad to be able to meet Korean adventurers for Korea's biggest holiday, Chuseok!
                return true;
            default:
                return true;
        }
    }
}
