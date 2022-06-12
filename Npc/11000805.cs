using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000805: Hozzie
/// </summary>
public class _11000805 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002966$
    // - H-how can I...? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002968$
                // - I don't care who you are. Just stop talking to me. They'll beat me up if they see me talking to you.
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
