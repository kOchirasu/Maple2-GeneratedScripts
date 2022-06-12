using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003786: Mason
/// </summary>
public class _11003786 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213192607009642$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213192607009643$
                // - There's work to be done.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
