using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000236: Jerome
/// </summary>
public class _11000236 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001007$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001010$
                // - Don't say anything. Just go.
                switch (selection) {
                    // $script:0831180407001011$
                    // - What are you doing?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407001012$
                // - I said go. Geez, this is such a mess! 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
