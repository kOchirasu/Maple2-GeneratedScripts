using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000673: Anonymous Prisoner's Diary
/// </summary>
public class _11000673 : NpcScript {
    internal _11000673(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002739$ 
                // - ...
                return true;
            case 10:
                // $script:0831180407002740$ 
                // - <font color="#909090">(This looks like an old journal. You open the faded cover and turn to a dusty page.)</font>
                // $script:0831180407002741$ 
                // - "When I discovered the secret passageway, I was excited beyond measure. I thought I could finally escape."
                // $script:0831180407002742$ 
                // - "But at the other end of the passageway, an endless abyss awaited me. Is it really impossible to escape from this misery?"
                return true;
            default:
                return true;
        }
    }
}
