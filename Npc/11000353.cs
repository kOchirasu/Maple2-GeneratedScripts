using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000353: Thompson
/// </summary>
public class _11000353 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001467$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001470$
                // - Our fuel needs are growing by the day. I think more excavation sites will be needed soon.
                return 30;
            case (30, 1):
                // $script:0831180407001471$
                // - We're pumping oil every day. It's still kind of surprising how much we need to get by.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
