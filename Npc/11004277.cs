using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004277: Keatle
/// </summary>
public class _11004277 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011275$
    // - I sssmell sssomething that doesssn't belong...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011276$
                // - I sssmell sssomething that doesssn't belong...
                return 10;
            case (10, 1):
                // $script:0911203207011277$
                // - A ssstranger? You mussst be fearlessss indeed to venture Nazkar unprepared.
                switch (selection) {
                    // $script:0911203207011278$
                    // - Hi! Who are you?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011279$
                // - A foolisssh quessstion. Tsssk. Then again, you are an ignorant fool, ssso it'sss to be expected. I watch over Nazkar!
                return 11;
            case (11, 1):
                // $script:0911203207011280$
                // - I've watched thisss place through countlesss lifetimesss. A hundred birthsss and deathsss, and ssstill the sssight assstoundsss me.
                switch (selection) {
                    // $script:0911203207011281$
                    // - Wow! Do sssnakes, I mean, snakes even live that long?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011282$
                // - Sssimple human, you ssstill think I'm just another sssnake... I will give you one warning: beware up ahead!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
