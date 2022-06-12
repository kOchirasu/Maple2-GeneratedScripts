using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000151: Cecilia
/// </summary>
public class _11000151 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000644$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000645$
                // - Out of my way.
                return -1;
            case (21, 0):
                // $script:0831180407000646$
                // - Go ask yourself.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (21, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
