using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000857: Monshel
/// </summary>
public class _11000857 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003115$
    // - I'm not doing this because I want to.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003118$
                // - Please. Please, don't stare.
                return 30;
            case (30, 1):
                // $script:0831180407003119$
                // - ...
                return 30;
            case (30, 2):
                // $script:0831180407003120$
                // - S-stop staring!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
