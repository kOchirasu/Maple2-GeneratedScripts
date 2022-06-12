using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000615: Kent
/// </summary>
public class _11000615 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002514$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002516$
                // - The empire turned its back on these people when they needed it the most. Someone had to step in and protect them. And the empire will get what it deserves.
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
