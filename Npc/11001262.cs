using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001262: Ripert
/// </summary>
public class _11001262 : NpcScript {
    internal _11001262(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203182807004698$ 
                // - Strength will win a fight. Information will win a war. 
                return true;
            case 30:
                // $script:1206005307004737$ 
                // - What do you wa—I mean, welcome, valued customer! What kind of information can I help you with today?
                switch (selection) {
                    // $script:1206005307004738$
                    // - What do you do here, exactly?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1206005307004739$ 
                // - This $map:52000020$ exists to provide only the most reliable information handpicked by the hundreds and thousands of members of the Barrota Trading Company, Victoria Island's largest community of traveling merchants.
                switch (selection) {
                    // $script:1206005307004740$
                    // - Okay, you've caught my attention.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1206010607004771$ 
                // - Of course! Our information is divided into five classes for your convenience: S, A, B, C, and D. The class varies with the quality and price of the information. Class D information starts from 1,000 mesos, while Class S information is a steal at 50 million mesos.
                // $script:1206010607004772$ 
                // - Now, what kind of information do you want?
                switch (selection) {
                    // $script:1206010607004773$
                    // - Class D please!
                    case 0:
                        Id = 33;
                        return false;
                    // $script:1206010607004774$
                    // - Class S! Only the best for me!
                    case 1:
                        Id = 34;
                        return false;
                    // $script:1206010607004775$
                    // - Oh, I was just browsing.
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1206011307004791$
                    // - I'll come back later.
                    case 3:
                        Id = 38;
                        return false;
                }
                return true;
            case 33:
                // $script:1206010607004776$ 
                // - What're you, a cheapskate? Look, I don't got time for... I mean, sorry, but I don't have any appointments available!
                switch (selection) {
                    // $script:1206010607004777$
                    // - I need to ask something else.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 34:
                // $script:1206010607004778$ 
                // - Absolutely! May I offer you a cup of tea? Or perhaps a moist towelette?
                switch (selection) {
                    // $script:1206010607004779$
                    // - Actually, I just remembered I've got other things to do.
                    case 0:
                        Id = 37;
                        return false;
                }
                return true;
            case 35:
                // $script:1206010607004780$ 
                // - This isn't an art gallery! Is wasting my time entertaining to you?
                switch (selection) {
                    // $script:1206010607004781$
                    // - I need to ask something else.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:1206010607004782$ 
                // - Which class of information would you like?
                switch (selection) {
                    // $script:1206010607004783$
                    // - Class D please!
                    case 0:
                        Id = 33;
                        return false;
                    // $script:1206010607004784$
                    // - Class S! Only the best for me!
                    case 1:
                        Id = 34;
                        return false;
                    // $script:1206010607004785$
                    // - Oh, I was just browsing.
                    case 2:
                        Id = 35;
                        return false;
                    // $script:1206011307004792$
                    // - I'll come back later.
                    case 3:
                        Id = 38;
                        return false;
                }
                return true;
            case 37:
                // $script:1206010607004786$ 
                // - Wait! If you'd just give me a moment... Bah!
                return true;
            case 38:
                // $script:1206011307004793$ 
                // - Yes, well, please come again!
                //   <font color="#909090">(He looks a bit crestfallen.)</font>
                return true;
            default:
                return true;
        }
    }
}
