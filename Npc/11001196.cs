using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001196: Grue
/// </summary>
public class _11001196 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004202$
    // - Let's have a look at the requisition form... <i>Are you kidding me?</i> I'm not dealing with this right now.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004205$
                // - Mm.. What? 
                //   Is there something you need?
                switch (selection) {
                    // $script:1016202007004206$
                    // - Show me what you have to sell.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004207$
                // - All right, have a looksie in my bag...
                return 31;
            case (31, 1):
                // $script:1016202007004208$
                // - ...Wait, what am I doing? I'm not some blasted shopkeep! I support the employees of the broadcasting station. Coffee, snacks, transportation, unsolicited advice. I get them whatever they need. I'm a key member of the team, so don't you forget it!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
