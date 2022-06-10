using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000110: Cavan
/// </summary>
public class _11000110 : NpcScript {
    internal _11000110(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000449$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000452$ 
                // - At least it's good to be on this big lump of land instead of that small island. I felt so trapped there.  
                return true;
            case 50:
                // $script:0831180407000453$ 
                // - Hey, did you see that $npcName:22300149$ over there? I thought they only had those in my hometown. I had no idea! 
                // $script:0831180407000454$ 
                // - Anything that reminds me of my hometown makes me happy. Like that $npcName:22300149$... I guess this is what it's like to be homesick.  
                return true;
            default:
                return true;
        }
    }
}
