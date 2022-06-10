using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004537: Barricade Defender
/// </summary>
public class _11004537 : NpcScript {
    internal _11004537(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104170807012611$ 
                // - We're doing our best to defend $map:02020041$!
                return true;
            case 10:
                // $script:0104170807012612$ 
                // - We're doing our best to defend $map:02020041$!
                // $script:0104170807012613$ 
                // - Send me to where the fighting's thickest! I'll crush any enemy in my path!
                // $script:0104170807012614$ 
                // - Umm... Would you mind taking a few of them out while you're here? N-not that I can't take them myself, of course!
                return true;
            default:
                return true;
        }
    }
}
