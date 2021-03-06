using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001059: Danak
/// </summary>
public class _11001059 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003617$
    // - Gasp! Did my wife send you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003620$
                // - No one understands the burning passion of this lonely man... Sigh... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
