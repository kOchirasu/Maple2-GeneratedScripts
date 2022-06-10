using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000047: Anna
/// </summary>
public class _11000047 : NpcScript {
    internal _11000047(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000215$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0831180407000218$ 
                // - I used to love hearing the sound of bow craftsmen carving wood. The most talented of them all was Freeman. 
                // $script:0831180407000219$ 
                // - He was $npcName:11000007[gender:1]$'s father. It's a shame an illness took him so early, but he would surely approve of the woman his daughter grew to be.
                return true;
            default:
                return true;
        }
    }
}
