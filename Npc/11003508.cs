using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003508: Sana
/// </summary>
public class _11003508 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0816160115009011$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009012$
                // - My parents ran this store before my brother inherited it. And now he's chasing his dream of turning it into a cafe or something...
                return -1;
            case (40, 0):
                // $script:0816160115009013$
                // - The cafe's being remodeled right now. You should swing by when it reopens!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
