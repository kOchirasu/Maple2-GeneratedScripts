using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004064: Molten Fountain
/// </summary>
public class _11004064 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010113$
    // - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010114$
                // - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010115$
                // - <font color="#909090">(A field journal's been left next to the fountain. It has Silver Wolf's name on it.)
                return 10;
            case (10, 2):
                // $script:0619202207010116$
                // - <i>For generations, we believed $map:02000046$ was a natural formation. However, I'm beginning to think otherwise...</i>
                return 10;
            case (10, 3):
                // $script:0619202207010117$
                // - <i>While scouting out the area, I noticed that the lava flows in a precise circular path. I scouted out the nearby cave systems, and I can find no source of the lava underground.</i>
                return 10;
            case (10, 4):
                // $script:0619202207010118$
                // - <i>This must be the work of powerful magic. If that's the case, then whoever did this must be trying to protect something within the Hourglass.</i>
                return 10;
            case (10, 5):
                // $script:0619202207010119$
                // - <i>I still don't know </i>why<i> the lava is circling the mountain, but whatever the reason, I'm sure it's important. And perhaps valuable...</i>
                return 10;
            case (10, 6):
                // $script:0619202207010120$
                // - <i>There's a lost temple that was used as a tomb for the great chieftains in ages past. Could this actually be the site of that temple? And how does one get inside...?</i>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Next,
            (10, 5) => NpcTalkButton.Next,
            (10, 6) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
