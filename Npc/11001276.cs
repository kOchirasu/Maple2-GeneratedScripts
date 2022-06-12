using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001276: Maccan
/// </summary>
public class _11001276 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1207124110001298$
    // - Ah! Ah! Ah-choo!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1223143510001417$
                // - Ah-ah-ah-achoo! So much salt in the air! It tickles my nose, but I love the taste. Is there something I can do for you?
                switch (selection) {
                    // $script:1223143510001418$
                    // - I want to go to Karkar Island.
                    case 0:
                        return 41;
                    // $script:1223143510001419$
                    // - ...
                    case 1:
                        return 44;
                }
                return -1;
            case (41, 0):
                // $script:1223143510001420$
                // - In that case, you'll want a ride in my <i>Lumiwind</i>. She's my greatest invention! Her design is inspired by the extinct dragons who once soared the skies, the lumarigons. Do you want to ride?
                switch (selection) {
                    // $script:1223143510001421$
                    // - Yes.
                    case 0:
                        return 42;
                    // $script:1223143510001422$
                    // - I'll come back later.
                    case 1:
                        return 43;
                }
                return -1;
            case (42, 0):
                // functionID=1 
                // $script:1223143510001423$
                // - All right, bon voyage!
                return -1;
            case (43, 0):
                // $script:1223143510001424$
                // - No rush. The <i>Lumiwind</i> will always be right here.
                return -1;
            case (44, 0):
                // $script:0215134610001837$
                // - Here to gawk at an old genius? You're silly, you know that?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Close,
            (44, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
