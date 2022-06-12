using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004139: Einos
/// </summary>
public class _11004139 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010549$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010550$
                // - It is all well and good to forget one's troubles in a cheerful place such as this, but we cannot lose sight of what's real. A dark storm gathers over Maple World. Now more than ever, we need heroes. Will you answer the call?
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
