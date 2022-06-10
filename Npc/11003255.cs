using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003255: Kaitlyn
/// </summary>
public class _11003255 : NpcScript {
    internal _11003255(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008178$ 
                // - What is it?
                return true;
            case 30:
                // $script:0403155707008179$ 
                // - There's no shame in asking for my help. I am, after all, the smartest person you know.
                // $script:0403155707008180$ 
                // - When you're done here, go ahead and help Professor $npcName:11003148[gender:0]$ with his research. He's been on edge lately thanks to his migraines. Don't do anything to make them worse, will you?
                // $script:0403155707008181$ 
                // - <font color="#909090">($npcName:11003254[gender:1]$ whispers to herself.) </font>
                //   <font size='20'>I wish he wore glasses. He's so intelligent and sensitive... It would be perfect...</font>
                return true;
            default:
                return true;
        }
    }
}
