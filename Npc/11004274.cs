using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004274: Cheche
/// </summary>
public class _11004274 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011259$
    // - What a wonderful, joyous day!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011260$
                // - What a wonderful, joyous day!
                switch (selection) {
                    // $script:0911203207011261$
                    // - What are you so happy about?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011262$
                // - Every day is a joy! I was sent up here because I was scared of the desert monsters, and at first, I was scared of being so high up, too... But I've adjusted!
                return 11;
            case (11, 1):
                // $script:0911203207011263$
                // - I'm overjoyed to be in such a safe place. Now I have friends and don't need to be scared of any monsters!
                return 11;
            case (11, 2):
                // $script:0913152507011309$
                // - Stay positive, and good fortune will follow! Never forget that, human!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
