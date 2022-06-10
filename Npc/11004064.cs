using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004064: Molten Fountain
/// </summary>
public class _11004064 : NpcScript {
    internal _11004064(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010113$ 
                // - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
                return true;
            case 10:
                // $script:0619202207010114$ 
                // - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
                // $script:0619202207010115$ 
                // - <font color="#909090">(A field journal's been left next to the fountain. It has Silver Wolf's name on it.)
                // $script:0619202207010116$ 
                // - <i>For generations, we believed $map:02000046$ was a natural formation. However, I'm beginning to think otherwise...</i>
                // $script:0619202207010117$ 
                // - <i>While scouting out the area, I noticed that the lava flows in a precise circular path. I scouted out the nearby cave systems, and I can find no source of the lava underground.</i>
                // $script:0619202207010118$ 
                // - <i>This must be the work of powerful magic. If that's the case, then whoever did this must be trying to protect something within the Hourglass.</i>
                // $script:0619202207010119$ 
                // - <i>I still don't know </i>why<i> the lava is circling the mountain, but whatever the reason, I'm sure it's important. And perhaps valuable...</i>
                // $script:0619202207010120$ 
                // - <i>There's a lost temple that was used as a tomb for the great chieftains in ages past. Could this actually be the site of that temple? And how does one get inside...?</i>
                return true;
            default:
                return true;
        }
    }
}
