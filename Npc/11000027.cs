using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000027: Corni
/// </summary>
public class _11000027 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000175$
    // - Yes? Yes? What do you need? How can I help?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000177$
                // - I messed up. I messed it all up. Woe is meee!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
