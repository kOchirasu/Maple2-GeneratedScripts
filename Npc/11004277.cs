using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004277: Keatle
/// </summary>
public class _11004277 : NpcScript {
    internal _11004277(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011275$ 
                // - I sssmell sssomething that doesssn't belong...
                return true;
            case 10:
                // $script:0911203207011276$ 
                // - I sssmell sssomething that doesssn't belong...
                // $script:0911203207011277$ 
                // - A ssstranger? You mussst be fearlessss indeed to venture Nazkar unprepared.
                switch (selection) {
                    // $script:0911203207011278$
                    // - Hi! Who are you?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011279$ 
                // - A foolisssh quessstion. Tsssk. Then again, you are an ignorant fool, ssso it'sss to be expected. I watch over Nazkar!
                // $script:0911203207011280$ 
                // - I've watched thisss place through countlesss lifetimesss. A hundred birthsss and deathsss, and ssstill the sssight assstoundsss me.
                switch (selection) {
                    // $script:0911203207011281$
                    // - Wow! Do sssnakes, I mean, snakes even live that long?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0911203207011282$ 
                // - Sssimple human, you ssstill think I'm just another sssnake... I will give you one warning: beware up ahead!
                return true;
            default:
                return true;
        }
    }
}
