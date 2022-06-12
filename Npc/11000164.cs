using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000164: Vale
/// </summary>
public class _11000164 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000694$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000697$
                // - Sigh... I knew this was a dangerous job, but I volunteered anyway because it pays twice as much as other jobs I've had. Maybe I shouldn't have taken it, though. I would've been safer hauling fish at the harbor.
                return -1;
            case (40, 0):
                // $script:0831180407000698$
                // - If not for the earthquake, the Royal Road wouldn't have been destroyed and I could've been in $map:02000001$ by now. I'd be done with my delivery, and kicking back while waiting for the court to open.
                return 40;
            case (40, 1):
                // $script:0831180407000699$
                // - Actually, if the supplies for the court weren't stolen to begin with, the palace wouldn't have needed the replacements in such a hurry. This is a mess.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
