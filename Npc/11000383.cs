using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000383: Norman
/// </summary>
public class _11000383 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001562$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001564$
                // - You're lucky I found you and that I'm a doctor. You could've been in big trouble. Stop being stupid, and listen to your parents!
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
