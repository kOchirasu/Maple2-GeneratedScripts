using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001381: Modir
/// </summary>
public class _11001381 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217192807005381$
    // - Hm? What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005724$
                // - I'm thinking up ways to bring prosperity to $map:02010036$. If you want to chat, talk to someone else.
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
