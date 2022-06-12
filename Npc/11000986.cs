using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000986: Shapian
/// </summary>
public class _11000986 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003398$
    // - That was the only way to show my gratitude... Sniff... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003400$
                // - There are many stones yet unknown to the world. The ones that shine aren't the only beautiful ones. 
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
